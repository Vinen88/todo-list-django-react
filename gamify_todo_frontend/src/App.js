import logo from './logo.svg';
import './App.css';
import react, { Component } from 'react';

const todoItems = [
  { id: 1, 
    title: 'Go to the store', 
    description: "I need to buy some groceries.",
    completed: false },
  { id: 2, 
    title: 'Go to the bank',
    description: "I need to deposit my paycheck.", 
    completed: false },
  { id: 3,
    title: 'Go to the doctor', 
    description: "I need to get a checkup.",
    completed: false },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      todoList: todoItems,
    };
  }

  displayCompleted = status => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
          onClick={() => this.displayCompleted(true)}
        >
          Complete
        </span>
      </div>
    )
}

