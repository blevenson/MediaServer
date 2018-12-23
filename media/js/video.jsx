import React from 'react';

class Video extends React.Component {
  constructor(props) {
    super(props);

    this.state = { 
      video: props.vid,
    };
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="videoPlayer">
        <video width="320" height="240" controls src={"/uploads/" + this.props.vid.file}></video>
        <p id="videoDescription">Description: {this.props.vid.description}</p>
      </div>
    );
  }
}

Video.propTypes = {
};

export default Video;
