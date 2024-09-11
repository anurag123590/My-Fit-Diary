

// Function to handle user registration
async function registerUser() {
    const userData = {
        name: document.getElementById("name").value,
        phone_number: parseInt(document.getElementById("phone_number").value),
        profile_picture: document.getElementById("profile_picture").value,
        working_out_from: document.getElementById("working_out_from").value,
        body_goal: document.getElementById("body_goal").value,
    };

    const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
    });

    if (response.ok) {
        console.log("User registered successfully");
    } else {
        console.error("Failed to register user");
    }
}

// Function to handle group creation
async function createGroup() {
    const groupData = {
        name: document.getElementById("group_name").value,
        description: document.getElementById("group_description").value,
        members: [
            { phone_number: parseInt(document.getElementById("member_phone").value) },
            // Add more members if needed
        ],
    };

    const response = await fetch("http://127.0.0.1:8000/api/create_group/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(groupData),
    });

    if (response.ok) {
        console.log("Group created successfully");
    } else {
        console.error("Failed to create group");
    }
}

// Function to handle post creation
async function createPost() {
    const postData = {
        content: document.getElementById("post_content").value,
        image_url: document.getElementById("post_image_url").value,
        user_id: parseInt(document.getElementById("post_user_id").value),
        group_id: parseInt(document.getElementById("post_group_id").value),
    };

    const response = await fetch("http://127.0.0.1:8000/api/posts/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(postData),
    });

    if (response.ok) {
        console.log("Post created successfully");
    } else {
        console.error("Failed to create post");
    }
}

// Function to handle daily question creation
async function createDailyQuestion() {
    const questionData = {
        workout_plan: document.getElementById("workout_plan").value,
        guilty_action: document.getElementById("guilty_action").value,
        user_id: parseInt(document.getElementById("question_user_id").value),
    };

    const response = await fetch("http://127.0.0.1:8000/api/daily_questions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(questionData),
    });

    if (response.ok) {
        console.log("Daily question created successfully");
    } else {
        console.error("Failed to create daily question");
    }
}
