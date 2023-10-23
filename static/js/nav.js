const chart = document.getElementById('chart');
const data = document.getElementById('data');
const cuttest = document.getElementById('cuttest');

// if (typeof Storage !== "undefined") {
//   // Add an event listener to the window's beforeunload event
//   window.addEventListener("beforeunload", function (event) {
//     localStorage.setItem('dataBColor', '#0E1117');
//     localStorage.setItem('cuttestBColor', '#0E1117');
//     localStorage.setItem('chartBColor', '#2D5A3D');  
//   });
// }

const chartBColor = localStorage.getItem('chartBColor');
const dataBColor = localStorage.getItem('dataBColor');
const cuttestBColor = localStorage.getItem('cuttestBColor');

if (dataBColor) {
  data.style.backgroundColor = dataBColor;
}

if (cuttestBColor) {
  cuttest.style.backgroundColor = cuttestBColor;
}

if (chartBColor) {
  chart.style.backgroundColor = chartBColor;
}

chart.addEventListener('click', function(event) {
  // Prevent the default action (page refresh or navigation)
  localStorage.setItem('dataBColor', '#0E1117');
  localStorage.setItem('cuttestBColor', '#0E1117');
  localStorage.setItem('chartBColor', '#2D5A3D');

  data.style.backgroundColor = dataBColor;
  cuttest.style.backgroundColor = cuttestBColor;

  chart.style.backgroundColor = chartBColor;
});

data.addEventListener('click', function(event) {
  // Prevent the default action (page refresh or navigation)
  localStorage.setItem('chartBColor', '#0E1117');
  localStorage.setItem('cuttestBColor', '#0E1117');
  localStorage.setItem('dataBColor', '#2D5A3D');

  chart.style.backgroundColor = chartBColor;
  cuttest.style.backgroundColor = cuttestBColor;

  data.style.backgroundColor = dataBColor;
});

cuttest.addEventListener('click', function(event) {
  localStorage.setItem('dataBColor', '#0E1117');
  localStorage.setItem('chartBColor', '#0E1117');
  localStorage.setItem('cuttestBColor', '#2D5A3D');

  data.style.backgroundColor = dataBColor;
  chart.style.backgroundColor = chartBColor;

  cuttest.style.backgroundColor = cuttestBColor ;
});

console.log("hello")