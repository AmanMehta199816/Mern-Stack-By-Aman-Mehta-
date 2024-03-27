Demo Project on Mern Stack Development 
Below is a basic MERN (MongoDB, Express.js, React.js, Node.js) stack demo project code. This demo project consists of a simple todo list application where users can add, delete, and mark todos as completed.

Backend (Node.js + Express.js):

```javascript
// server.js

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// MongoDB Configuration
mongoose.connect('mongodb://localhost:27017/mern_demo', { useNewUrlParser: true, useUnifiedTopology: true });
const connection = mongoose.connection;
connection.once('open', () => {
    console.log('MongoDB database connection established successfully');
});

// Todo Model
const Todo = require('./models/todo.model');

// API Routes
const todoRouter = require('./routes/todo');
app.use('/todos', todoRouter);

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```javascript
// models/todo.model.js

const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const todoSchema = new Schema({
    description: { type: String, required: true },
    completed: { type: Boolean, default: false }
}, {
    timestamps: true
});

const Todo = mongoose.model('Todo', todoSchema);

module.exports = Todo;
```

```javascript
// routes/todo.js

const express = require('express');
const router = express.Router();
const Todo = require('../models/todo.model');

// Get all todos
router.route('/').get((req, res) => {
    Todo.find()
        .then(todos => res.json(todos))
        .catch(err => res.status(400).json('Error: ' + err));
});

// Add new todo
router.route('/add').post((req, res) => {
    const description = req.body.description;
    const newTodo = new Todo({ description });

    newTodo.save()
        .then(() => res.json('Todo added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});

// Delete todo
router.route('/:id').delete((req, res) => {
    Todo.findByIdAndDelete(req.params.id)
        .then(() => res.json('Todo deleted.'))
        .catch(err => res.status(400).json('Error: ' + err));
});

// Update todo
router.route('/update/:id').post((req, res) => {
    Todo.findById(req.params.id)
        .then(todo => {
            todo.description = req.body.description;
            todo.completed = req.body.completed;

            todo.save()
                .then(() => res.json('Todo updated!'))
                .catch(err => res.status(400).json('Error: ' + err));
        })
        .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;
```

Frontend (React.js):

```javascript
// App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [description, setDescription] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/todos/')
      .then(response => {
        setTodos(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const addTodo = () => {
    axios.post('http://localhost:5000/todos/add', { description })
      .then(res => {
        console.log(res.data);
        setTodos([...todos, { description, _id: res.data }]);
        setDescription('');
      })
      .catch(err => console.log(err));
  };

  const deleteTodo = (id) => {
    axios.delete(`http://localhost:5000/todos/${id}`)
      .then(res => {
        console.log(res.data);
        setTodos(todos.filter(todo => todo._id !== id));
      })
      .catch(err => console.log(err));
  };

  const handleInputChange = (e) => {
    setDescription(e.target.value);
  };

  return (
    <div>
      <h1>MERN Stack Todo App</h1>
      <input type="text" value={description} onChange={handleInputChange} />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map(todo => (
          <li key={todo._id}>
            {todo.description}
            <button onClick={() => deleteTodo(todo._id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

This demo project sets up a simple MERN stack todo list application where users can add new todos, delete existing todos, and view the list of todos. The backend server is built with Node.js and Express.js, connected to a MongoDB database, while the frontend is developed using React.js. You can further expand and customize this project according to your requirements.
