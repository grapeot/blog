import * as THREE from 'three';
import { GeometryFactory } from './utils/GeometryFactory.ts';
import { MaterialFactory } from './utils/MaterialFactory.ts';

// Constants for animation timing
const FPS = 30;
const FRAME_TIME = 1000 / FPS; // 33.33ms per frame
const SAMPLES_PER_SECOND = 10;
const SAMPLE_INTERVAL = 1000 / SAMPLES_PER_SECOND; // 100ms per sample
const FADE_FRAMES = 15;
const CIRCLE_RADIUS = 2;

// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

// Camera setup for proper circle viewing
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Renderer setup with proper materials support
const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
document.body.appendChild(renderer.domElement);

// Lighting setup for metallic materials
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);

// Create base circle
const circle = GeometryFactory.createCircle(CIRCLE_RADIUS);
scene.add(circle);

// Create fixed point at top of circle
const fixedPoint = GeometryFactory.createPoint(
  new THREE.Vector3(0, CIRCLE_RADIUS, 0)
);
scene.add(fixedPoint);

// Chord management
interface ActiveChord {
  line: THREE.Line;
  frameCount: number;
  material: THREE.LineBasicMaterial;
}

const activeChords: ActiveChord[] = [];

// Create new chord with random point
function createNewChord() {
  const randomPoint = GeometryFactory.getRandomPointOnCircle(CIRCLE_RADIUS);
  const sampledPoint = GeometryFactory.createPoint(randomPoint);
  scene.add(sampledPoint);

  // Create highlighted chord
  const chord = GeometryFactory.createChord(
    fixedPoint.position,
    randomPoint,
    1.0
  );
  scene.add(chord);

  // Add to active chords
  activeChords.push({
    line: chord,
    frameCount: 0,
    material: chord.material as THREE.LineBasicMaterial
  });

  // Remove sampled point after a brief delay
  setTimeout(() => {
    scene.remove(sampledPoint);
  }, FRAME_TIME * 2);
}

// Handle window resizing
window.addEventListener('resize', () => {
  const width = window.innerWidth;
  const height = window.innerHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
});

// Animation timing variables
let lastFrameTime = 0;
let lastSampleTime = 0;

// Animation loop with precise frame timing
function animate(currentTime: number) {
  requestAnimationFrame(animate);

  // Ensure consistent frame rate
  if (currentTime - lastFrameTime < FRAME_TIME) {
    return;
  }

  // Update timing
  lastFrameTime = currentTime;

  // Check if it's time for a new sample
  if (currentTime - lastSampleTime >= SAMPLE_INTERVAL) {
    lastSampleTime = currentTime;
    createNewChord();
  }

  // Update active chords
  for (let i = activeChords.length - 1; i >= 0; i--) {
    const chord = activeChords[i];
    chord.frameCount++;

    if (chord.frameCount >= FADE_FRAMES) {
      // Set final dark green state with semi-transparency
      chord.material.color.setHex(0x004400);
      chord.material.opacity = 0.3;
    } else {
      // Gradually transition from gold to dark green
      const progress = chord.frameCount / FADE_FRAMES;
      const startColor = new THREE.Color(0xFFD700);
      const endColor = new THREE.Color(0x004400);
      chord.material.color.copy(startColor).lerp(endColor, progress);
      chord.material.opacity = 1.0 - (0.7 * progress);
    }
  }

  renderer.render(scene, camera);
}

// Start the animation loop
animate(0);
