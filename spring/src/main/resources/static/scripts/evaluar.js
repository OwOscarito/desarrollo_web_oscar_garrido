
currentActivityId = null;

function open_evaluation(element) {
    const evaluationDialog = document.getElementById('evaluation-dialog');
    currentActivityId = element.getAttribute('data-id');
    const evaluationForm = document.getElementById('evaluation-form');
    if (evaluationForm) {
        evaluationForm.reset();
        evaluationForm.style.display = 'block';
    }
    evaluationDialog.showModal();
}

function reload_grade(activityId) {
    const gradeElement = document.getElementById('grade-' + activityId);
    fetch('/nota/' + activityId)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                gradeElement.textContent = data.nota;
            } else {
                console.error('Error fetching grade:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}


function send_evaluation(evaluationForm) {
    const formData = new FormData(evaluationForm);
    formData.append('activityId', currentActivityId);
    
    return fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => true)
    .catch(error => false);
}

