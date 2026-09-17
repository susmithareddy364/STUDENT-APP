const form = document.getElementById("studentForm");


// Save student
form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        age: document.getElementById("age").value,
        course: document.getElementById("course").value
    };


    const response = await fetch("/api/students", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(student)

    });


    if (response.ok) {

        alert("Student saved successfully!");

        form.reset();

        loadStudents();
    }

});


// Get students
async function loadStudents() {

    const response = await fetch("/api/students");

    const students = await response.json();

    const table = document.getElementById("studentTable");

    table.innerHTML = "";


    students.forEach(function(student) {

        const row = `
            <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.email}</td>
                <td>${student.age}</td>
                <td>${student.course}</td>
            </tr>
        `;

        table.innerHTML += row;

    });

}


// Load students when page opens
loadStudents();