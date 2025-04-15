// script.js

// Sample data for businesses
const businesses = [
  {
    name: "Lagos Bites",
    description: "Popular Nigerian dishes with 500+ reviews.",
    category: "Restaurants"
  },
  {
    name: "CodeTech Hub",
    description: "Best software solutions in town.",
    category: "Technology"
  },
  {
    name: "FashionNova NG",
    description: "Trendy outfits, great prices, and awesome service.",
    category: "Fashion"
  },
  {
    name: "Health First Clinic",
    description: "Top-rated health services and wellness.",
    category: "Health"
  },
  {
    name: "SmartLearn Academy",
    description: "Innovative e-learning and tutoring center.",
    category: "Education"
  }
];

// Load businesses into the page
function loadBusinesses(filter = '') {
  const container = document.getElementById('businessList');
  container.innerHTML = '';

  const filtered = businesses.filter(biz =>
    biz.name.toLowerCase().includes(filter.toLowerCase()) ||
    biz.description.toLowerCase().includes(filter.toLowerCase()) ||
    biz.category.toLowerCase().includes(filter.toLowerCase())
  );

  if (filtered.length === 0) {
    container.innerHTML = '<p>No businesses found.</p>';
    return;
  }

  filtered.forEach(biz => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <h4>${biz.name}</h4>
      <p>${biz.description}</p>
      <small><strong>Category:</strong> ${biz.category}</small>
    `;
    container.appendChild(card);
  });
}

// Handle search
document.getElementById('searchInput').addEventListener('input', (e) => {
  loadBusinesses(e.target.value);
});

// Handle category filter
document.querySelectorAll('.category-btn').forEach(button => {
  button.addEventListener('click', () => {
    const category = button.textContent;
    loadBusinesses(category);
  });
});

// Initial load
window.addEventListener('DOMContentLoaded', () => {
  loadBusinesses();
});
