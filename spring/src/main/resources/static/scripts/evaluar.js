function submitAsyncPost(url, formData) {
    return fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => { return data })
    .catch(error => { return error });
}

currentActivityId = null;

function open_evaluation(activityId) {
    const evaluationDialog = document.getElementById('evaluation-dialog');
    const evaluationForm = document.getElementById('evaluation-form');
    if (evaluationForm) {
        evaluationForm.reset();
        evaluationForm.style.display = 'block';
    }

}

function send_evaluation(evaluationForm) {

}