const weekdayChart = document.getElementById("weekday-chart");
const activityChart = document.getElementById("activity-chart");
const timeChart = document.getElementById("time-chart");

new Chart(weekdayChart, {
  type: "line",
  data: {
    labels: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
    datasets: [
      {
        label: "# de Actividades",
        data: [12, 19, 3, 5, 2, 3, 9],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

new Chart(activityChart, {
  type: "pie",
  data: {
    labels: ["música", "deporte", "ciencias", "religión", "política", 
      "tecnología", "juegos", "baile", "comida", "otro"],
    datasets: [{
      label: "Número de Actividades",
      data: [30, 25, 20, 15, 10, 32, 10, 23, 12, 14, 8],
    },
    ]
  },
});

new Chart(timeChart, {
  type: "bar",
  data: {
    labels: ["Enero", "Febrero", "Marzo", "Abril"],
    datasets: [
      {
        label: "Mañana",
        data: [5, 6, 3, 5, 2],
        borderWidth: 1,
      },
      {
        label: "Mediodia",
        data: [12, 19, 15, 16, 11],
        borderWidth: 1,
      },
      {
        label: "Tarde",
        data: [8, 5, 7, 9, 4],
        borderWidth: 1,
      },
    ],
  },
});
