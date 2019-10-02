
Chart.defaults.global.defaultFontColor = '#333844';
Chart.defaults.global.defaultFontFamily = 'SinkinSans';
Chart.defaults.global.defaultFontSize = 10;

// Ruas com mais alojamentos

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'horizontalBar',
  data: {
      labels: ['Rua de Santa Catarina', 'Rua da Alegria', 'Rua do Almada', 
               'Av. da  Boavista', 'Rua de Santo Ildefonso','Rua de Cedofeita',
               'Rua do Bonjardim','Rua Formosa','Rua do Visconde de Setúbal'],
      datasets: [{
          label: 'Número de Anúncios',
          data: [179,130,126,116,105,101,98,97,94],
          backgroundColor: 'rgba(255, 105, 89, 1)',
          borderWidth: 1         
      }]
  },
  options: {
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }],
          xAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      },
      responsive: true,
      legend: {
	      position: 'bottom',
          labels: {
            fontSize: 13
          },
      }
  }
});

// Apartamentos, quartos privados e quartos partilhados

  var ctx = document.getElementById('myChart2').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Apartamentos Completos', 'Quartos Privativos', 'Quartos Partilhados'],
      datasets: [{
        label: 'Número de Alojamentos',
        data: [4002,494,14],
        backgroundColor: [
          'rgba(255, 105, 89, 1)',
          'rgba(24, 235, 198, 1)',
          'rgba(252,100,45,1)'
        ]

      }]
    },
    options: {
      responsive: true,
      legend: {
	      position: 'bottom',
	      labels: {
            fontSize: 13
          },
      }
    }
  });


// Utilizadores com mais anúncios/propriedades

  var ctx = document.getElementById('myChart3').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
      labels: ['Feels Like Home', 'Liiiving', 'Oporto City Flats', 
               'Host Wise', 'Porto City Hosts','Oporto Rental Management',
               'Home Me','Rui','Marta','Carolina'],
      datasets: [{
        label: 'Número de Anúncios',
        data: [53,49,45,42,39,35,28,28,27,26],
        backgroundColor: 
        'rgba(24, 235, 198, 1)'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }],
          xAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      },
      responsive: true,
      legend: {
	      position: 'bottom',
          labels: {
            fontSize: 13
          },
      }
    }
  });




