import * as THREE from 'three';

export class MaterialFactory {
  static createMetallicMaterial(color: number, opacity: number = 1.0): THREE.MeshStandardMaterial {
    return new THREE.MeshStandardMaterial({
      color: color,
      metalness: 0.8,
      roughness: 0.2,
      transparent: true,
      opacity: opacity,
    });
  }

  static createLineMaterial(color: number, opacity: number = 1.0): THREE.LineBasicMaterial {
    return new THREE.LineBasicMaterial({
      color: color,
      transparent: true,
      opacity: opacity,
    });
  }

  static createGlowMaterial(opacity: number = 1.0): THREE.ShaderMaterial {
    return new THREE.ShaderMaterial({
      uniforms: {
        color: { value: new THREE.Color(0xFFD700) },
        opacity: { value: opacity }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          gl_PointSize = 35.0;
        }
      `,
      fragmentShader: `
        uniform vec3 color;
        uniform float opacity;
        varying vec2 vUv;
        void main() {
          float dist = length(gl_PointCoord - vec2(0.5));
          float alpha = 1.0 - smoothstep(0.0, 0.7, dist);
          float intensity = 1.5;
          gl_FragColor = vec4(color * intensity, opacity * alpha);
        }
      `,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending
    });
  }
}
