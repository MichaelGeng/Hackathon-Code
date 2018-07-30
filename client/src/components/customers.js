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
    fetch('/api/customers')
      console.log('okay we fetched')
  }

  render() {
    return (
      <div>
        <h2>Customers</h2>
        <ul>
          <h1>Fullstack app working</h1>
        </ul>
      </div>
    );
  }
}

export default Customers;
