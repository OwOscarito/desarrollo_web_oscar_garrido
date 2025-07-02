let day_chart;
document.addEventListener('DOMContentLoaded', function () {
  day_chart = Highcharts.chart('day-chart', {
    chart: {
      type: 'line'
    },
    title: {
      text: 'Actividades por día'
    },
    xAxis: {
      title: {
        text: 'Dia'
      },
      categories: [],
    },
    yAxis: {
      title: {
        text: 'N° Actividades'
      }
    },
    series: [{
      name: 'N° Actividades',
      data: []
    }]
  });
});

let topic_chart;
document.addEventListener('DOMContentLoaded', function () {
  topic_chart = Highcharts.chart('topic-chart', {
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Actividades por tema'
    },
    series: [{}]
  });
});

let time_chart;
document.addEventListener('DOMContentLoaded', function () {
  time_chart = Highcharts.chart('time-chart', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Actividades por día de la semana'
    },
    xAxis: {
      title: {
        text: 'Dia'
      },
      categories: [],
    },
    yAxis: {
      title: {
        text: 'N° Actividades'
      }
    },
    series: [{
      name: 'Mañana',
      data: []
    },
    {
      name: 'Mediodia',
      data: []
    },
    {
      name: 'Tarde',
      data: []
    }]
  });
});

updateDayChart = () => {
  const url = '/estadisticas/dia';
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log("Data received:", data);
      day_chart.update({
        xAxis: {
          categories: data["days"]
        },
        series: [{
          data: data["count"]
        }]
      });
    })
    .catch(error => {
      console.error("Error receiving response:", error);
      return null;
    });
}

updateTopicChart = () => {
  const url = '/estadisticas/tema';
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log("Data received:", data);
      topic_chart.update({
        series: [{
          name: "N° Actividades",
          data: data
        }]
      });
    })
    .catch(error => {
      console.error("Error receiving response:", error);
      return null;
    });
}

updateTimeChart = () => {
  const url = '/estadisticas/tiempo';
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log("Data received:", data);
      time_chart.update({
        xAxis: {
          categories: data["year-month"]
        },
        series: data["series"]
      });
    })
    .catch(error => {
      console.error("Error receiving response:", error);
      return null;
    });
}


window.onload = () => {
  updateDayChart();
  updateTopicChart();
  updateTimeChart();
}