/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./cedossa/templates/**/*.html",
    "./cedossa/static/js/**/*.js",
    "./**/templates/**/*.html" // Wider search pattern
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

