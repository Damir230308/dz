import logo from './logo.svg';
import React from 'react';
import './App.css';
import AuthorList from './components/Author2.js';
import axios from 'axios'
import BookList from './components/Books';
import {ReactDOM} from 'react';
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from 'react-router-dom';
import AuthorBookList from './components/AuthorBook';
import LoginForm from './components/Auth';

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

//load_data() {
  //    axios.get('http://127.0.0.1/api/authors')
   // .then(respounse => {
    //  const authors = respounse.data
     // this.setState(
     //   {
      //  authors: authors['results']
     // }
   // )
    //}).catch(error => console.log(error))
   //     axios.get('http://127.0.0.1/api/book')
   // .then(respounse => {
    //  const books = respounse.data
     // this.setState(
      //  {
      //  books: books['results']
      //}
    //)
    //}).catch(error => console.log(error))
//}
  
  
  //componentDidMount() {
   // this.load_data()
  //}

  render () {
    return (
      <div className="App">
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to= '/'>Authors</Link>
              </li>
              <li>
                <Link to='/books'>Books</Link>
              </li>
              <li>
                <Link to='/login'>Login</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/'component={() => <AuthorList authors={this.state.authors} />} />
            <Route exact path='/author/:id' component ={() =><AuthorBookList items={this.state.books} />} />
            <Route exact path='/books'component={() => <BookList items={this.state.books} />} />
            <Route exact path='/login'component={() => <LoginForm />} />
            <Route component={NotFound404}/>
          </Switch>
        </BrowserRouter>
        <h2>Authors</h2>
        <AuthorList authors={this.state.authors} />
        <h2>Books</h2>
        <BookList items = {this.state.books} />
      </div>
    )
  }
}

export default App
