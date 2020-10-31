import logo from "./logo.svg";
import "./App.css";
import React from "react";

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      start_time: 0,
      ran_once: false,
      counting: false,
      true_duration: 0,
      reaction_time: 0,
      color: "green",
    };
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    // TODO: Your code here!
  };
  start_count() {
    this.setState(
      {
        start_time: window.performance.now(),
        counting: true,
        true_duration: Math.random() * 5000 + 2000, //(in ms)
        color: "red",
      },
      () => {
        setTimeout(() => {
          this.setState({
            color: "green",
          });
        }, this.state.true_duration);
      }
    );
    // TODO: Your code here!
  }

  setupActivator() {
    setTimeout(this.activateColor, this.state.true_duration);
  }

  activateColor() {
    this.setState({
      color: "green",
    });
  }

  end_count() {
    if (
      window.performance.now() - this.state.start_time >=
      this.state.true_duration
    ) {
      this.setState(
        {
          ran_once: true,
          counting: false,
          reaction_time:
            window.performance.now() -
            this.state.start_time -
            this.state.true_duration, //apparently bad
          color: "green",
        },
        () => {
          console.log(this.state);
          console.log(window.performance.now());
        }
      );
    }
    // TODO: Your code here!
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }

  render() {
    let msg;
    if (this.state.counting) {
      if (this.state.color === "red") {
        msg = "Wait for green";
      } else {
        msg = "Click!";
      }
    } else if (this.state.ran_once) {
      msg = `Your reaction time is ${Math.round(this.state.reaction_time)} ms`;
    } else {
      msg = "Click me to begin!";
    }
    // TODO: Your code here!
    return (
      <div
        className="PanelContainer"
        onClick={this.process_click}
        style={{ background: this.state.color }}
      >
        <div className="Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>
          Click as soon as the red box turns green. Click anywhere in the box to
          start.
        </p>
      </header>
    </div>
  );
}

export default App;
