import logo from './logo.svg';
import React from 'react';
import './App.css';
import AuthorList from './components/Author2.js';
import axios from 'axios'
import BookList from './components/Books';
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from 'react-router-dom';
import AuthorBookList from './components/AuthorBook';

const NotFound404 = ({ location }) => {
  return (
    <div>
    <h1>Страница по адресу `{location.pathname}` не найдена</h1>
  </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': [],
      'books': []
    }
  }
  
  
  componentDidMount() {
    axios.get('http://127.0.0.1/api/authors').then(respounse => {
      const authors = respounse.data
      this.setState({
        authors: authors
      })
    })
  }

  render () {
    return (
      <div className="App">
        <AuthorList authors={this.state.authors} />
        <BookList items = {this.state.books} />
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to= '/'>Authors</Link>
              </li>
              <li>
                <Link to='/books'>Books</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/'component={() => <AuthorList authors={this.state.authors} />} />
            <Route exact path='/author/:id' component ={() =><AuthorBookList items={this.state.books} />} />
            <Route exact path='/books'component={() => <BookList items={this.state.books} />} />
            <Redirect from='/authors' to='/'/>
            <Route component={NotFound404}/>
          </Switch>
        </BrowserRouter>
      </div>
    )
  }
}

export default App

