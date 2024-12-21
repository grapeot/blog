import * as THREE from 'three';
import { MaterialFactory } from './MaterialFactory';

export class GeometryFactory {
  static createCircle(radius: number = 2, segments: number = 64): THREE.Line {
    const geometry = new THREE.BufferGeometry();
    const points: THREE.Vector3[] = [];

    for (let i = 0; i <= segments; i++) {
      const theta = (i / segments) * Math.PI * 2;
      points.push(new THREE.Vector3(
        radius * Math.cos(theta),
        radius * Math.sin(theta),
        0
      ));
    }

    geometry.setFromPoints(points);
    const material = MaterialFactory.createMetallicMaterial(0x444444);
    return new THREE.Line(geometry, material);
  }

  static createPoint(position: THREE.Vector3): THREE.Points {
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.Float32BufferAttribute([
      position.x, position.y, position.z
    ], 3));

    const material = MaterialFactory.createGlowMaterial(1.0);
    return new THREE.Points(geometry, material);
  }

  static createChord(start: THREE.Vector3, end: THREE.Vector3, opacity: number = 1): THREE.Line {
    const geometry = new THREE.BufferGeometry();
    geometry.setFromPoints([start, end]);
    const material = MaterialFactory.createLineMaterial(0xFFD700, opacity); // Golden color to match points
    return new THREE.Line(geometry, material);
  }

  static getRandomPointOnCircle(radius: number = 2): THREE.Vector3 {
    const theta = Math.random() * Math.PI * 2;
    return new THREE.Vector3(
      radius * Math.cos(theta),
      radius * Math.sin(theta),
      0
    );
  }
}
