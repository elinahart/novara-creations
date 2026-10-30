// Attrape les étoiles : déplace le panier (souris ou flèches), chaque étoile attrapée rapporte un point.
const canvas = document.getElementById("jeu");
const ctx = canvas.getContext("2d");
const panier = { x: 240, w: 60 };
let etoiles = [];
let score = 0;
let gauche = false;
let droite = false;

addEventListener("keydown", (e) => { if (e.key === "ArrowLeft") gauche = true; if (e.key === "ArrowRight") droite = true; });
addEventListener("keyup", (e) => { if (e.key === "ArrowLeft") gauche = false; if (e.key === "ArrowRight") droite = false; });
canvas.addEventListener("pointermove", (e) => { panier.x = (e.offsetX / canvas.clientWidth) * canvas.width; });

function etoile(x, y) {
  ctx.fillStyle = "#ffd84a";
  ctx.fillRect(x - 2, y - 6, 4, 12);
  ctx.fillRect(x - 6, y - 2, 12, 4);
}

let dernier = performance.now();
function boucle(maintenant) {
  const dt = Math.min(0.05, (maintenant - dernier) / 1000);
  dernier = maintenant;
  panier.x += ((droite ? 1 : 0) - (gauche ? 1 : 0)) * 300 * dt;
  panier.x = Math.max(panier.w / 2, Math.min(canvas.width - panier.w / 2, panier.x));
  if (Math.random() < dt * 1.5) etoiles.push({ x: 20 + Math.random() * (canvas.width - 40), y: -10, v: 80 + Math.random() * 60 });
  etoiles = etoiles.filter((s) => {
    s.y += s.v * dt;
    if (s.y > canvas.height - 30 && Math.abs(s.x - panier.x) < panier.w / 2) { score++; return false; }
    return s.y < canvas.height + 10;
  });
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  etoiles.forEach((s) => etoile(s.x, s.y));
  ctx.fillStyle = "#c97b3d";
  ctx.fillRect(panier.x - panier.w / 2, canvas.height - 24, panier.w, 14);
  ctx.fillStyle = "#fff";
  ctx.font = "16px system-ui";
  ctx.fillText(`Étoiles : ${score}`, 12, 24);
  requestAnimationFrame(boucle);
}
requestAnimationFrame(boucle);
