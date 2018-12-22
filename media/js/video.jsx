import React from 'react';

class Video extends React.Component {
  constructor(props) {
    super(props);

    this.state = { 
      url: props.url,
      description: "Description",
    };
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="videoPlayer">
        <video width="320" height="240" controls src={this.props.url}></video>
        <p id="videoDescription">Description: {this.state.description}</p>
      </div>
    );
  }
}

Video.propTypes = {
};

export default Video;
