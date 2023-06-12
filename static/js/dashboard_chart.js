const ctx = document.getElementById('sensor_data');


new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'a',
      data: [12, 319, 3, 5, 2, 3],
      borderWidth: 1,
      borderColor: '#FFC100'
    },
    {
      label: 'b',
      data: [12, 119, 3, 5, 2, 3],
      borderWidth: 1,
      borderColor: '#C356EA'
    },
    {
      label: 'c',
      data: [12, 219, 3, 5, 2, 3],
      borderWidth: 1,
      borderColor: '#8FF243'
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});