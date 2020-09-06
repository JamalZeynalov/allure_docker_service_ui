function delProject(project_id) {
    let r = confirm("Are you sure you want to delete \'" + project_id + "\' report?");
    if (r) {
        let xhr = new XMLHttpRequest();

        xhr.open('GET', '/delete/' + project_id, false);
        xhr.send();

        if (xhr.status !== 200) {
            alert(xhr.status + ': ' + xhr.statusText);
        } else {
            alert("Report \'" + project_id + "\' has been successfully removed.");
            document.location.reload();
        }
    }
}