import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  // Local state for the input field and tasks list
  const [taskInput, setTaskInput] = useState("");
  const [tasks, setTasks] = useState([]);

  // Fetch the current tasks from the Flask backend
  const fetchTasks = () => {
    fetch("/api/tasks")
      .then((res) => res.json())
      .then((data) => setTasks(data.tasks))
      .catch((err) => console.error(err));
  };

  // Run once on component mount
  useEffect(() => {
    fetchTasks();
  }, []);

  // Function to add a task
  const addTask = () => {
    if (!taskInput.trim()) return; // avoid adding empty tasks

    fetch("/api/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: taskInput }),
    })
      .then((res) => res.json())
      .then((data) => {
        setTasks(data.tasks);
        setTaskInput(""); // clear input after adding
      })
      .catch((err) => console.error(err));
  };

  // Function to remove a task
  const removeTask = (task) => {
    fetch("/api/tasks", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task }),
    })
      .then((res) => res.json())
      .then((data) => setTasks(data.tasks))
      .catch((err) => console.error(err));
  };

  return (
    <div>
      {/* Header */}
      <div className="header">To Do List Application</div>
  
      <div className="App">
        {/* Input field and Add button */}
        <div>
          <input
            type="text"
            placeholder="Enter Task"
            value={taskInput}
            onChange={(e) => setTaskInput(e.target.value)}
          />
          <button onClick={addTask}>Add Task</button>
        </div>
  
        {/* Task List */}
        <div className="task-list">
          {tasks.length === 0 ? (
            <p>No tasks yet.</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Task</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                {tasks.map((task, index) => (
                  <tr key={index}>
                    <td>{task}</td>
                    <td>
                      <button onClick={() => removeTask(task)}>Remove</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
