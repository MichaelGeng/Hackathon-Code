import React, { Component } from 'react';
import './customers.css';

class Customers extends Component {
  constructor() {
    super();
    this.state = {
      customers: []
    };
  }

  componentDidMount() {
    fetch('/api/users')
      .then(res => res.json())
      .then(customers => this.setState({customers}, () =>('Customers fetched', customers)));
      console.log(JSON);

  }

  render() {
    return (
      <div>
        <h2>Customers</h2>
        <ul>
          <h1>Fullstack app working</h1>
          {this.state.customers}
        </ul>
      </div>
    );
  }
}

export default Customers;
