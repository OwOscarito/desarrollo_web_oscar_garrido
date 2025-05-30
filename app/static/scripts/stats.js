document.addEventListener('DOMContentLoaded', function () {
  const day_chart = Highcharts.chart('day-chart', {
    chart: {
      type: 'line'
    },
    title: {
      text: 'Actividades por día de la semana'
    },
    xAxis: {
      title: {
        text: 'Dia'
      },
      categories: [1,2,3,4,5,6,7],
    },
    yAxis: {
      title: {
        text: 'N° Actividades'
      }
    },
    series: [{
      name: 'N° Actividades',
      data: [1, 0, 4, 1, 0, 4, 0]
    }]
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const topic_chart = Highcharts.chart('topic-chart', {
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Actividades por tema'
    },
    xAxis: {
      title: {
        text: 'Temas'
      },
      categories: ["Música", "Deporte", "Ciencias", "Religión", "Política", 
        "Tecnología", "Juegos", "Baile", "Comida", "Otro"]
    },
    yAxis: {
      title: {
        text: 'N° Actividades'
      }
    },
    series: [{
      name: 'N° Actividades',
      data: [1, 0, 4, 1, 0, 4, 0, 0, 4, 0]
    }]
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const time_chart = Highcharts.chart('time-chart', {
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
      categories: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
    },
    yAxis: {
      title: {
        text: 'N° Actividades'
      }
    },
    series: [{
      name: 'N° Actividades',
      data: [1, 0, 4, 1, 0, 4, 0]
    }]
  });
});
queryData = function (url) {
  fetch(url)
    .then(response => response.json())
    .then(comments => {
      console.log(comments);
      if (comments.length == 0) {
        const commentNotice = document.createElement("p");
        commentNotice.className = "notice";
        commentNotice.textContent = "No hay comentarios.";
        commentsContainer.appendChild(commentNotice);
        return;
      }
      for (const index in comments) {
        if (comments.hasOwnProperty(index)) {
          var comment = comments[index];
          const commentElement = document.createElement("article");

          const commentName = document.createElement("h4");
          commentName.textContent = index + ". " + comment["name"];
          commentElement.appendChild(commentName);

          const commentText = document.createElement("p");
          commentText.textContent = comment["text"];
          commentElement.appendChild(commentText);

          const commentDate = document.createElement("p");
          commentDate.textContent = new Date(comment["date"]).toLocaleString();
          commentElement.appendChild(commentDate);

          commentsContainer.appendChild(commentElement);
        }
      }
    })
    .catch(error => {
      console.error("Error loading graph:", error);
    });
}
