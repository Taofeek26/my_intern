import React, { Component } from "react";
import { render } from "react-dom";
import User from "./User";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
      return(
      <div>
        <User />
      </div>
      );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);