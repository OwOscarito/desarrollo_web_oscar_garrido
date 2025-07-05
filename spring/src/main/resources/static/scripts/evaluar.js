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
    fetch('/api/nota/' + activityId)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                gradeElement.textContent = data.nota;
            } else {
                console.error('Error fetching grade:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}

function send_evaluation() {
    const formData = new FormData();

    const selectedGrade = document.querySelector('input[name="grade"]:checked');
    
    if (!selectedGrade) {
        console.log('No grade selected');
        return;
    }
    
    console.log('Selected grade:', selectedGrade.value);
    formData.append('actividad-id', currentActivityId);
    formData.append('nota', selectedGrade.value);
    
    const url = '/api/nota/añadir';
    fetch(url, {
        method: 'POST',
        body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Grade sent successfully');
                reload_grade(currentActivityId);
                const evaluationDialog = document.getElementById('evaluation-dialog');
                evaluationDialog.close();
            } else {
                console.error('Error:', data.error || 'Unknown error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
