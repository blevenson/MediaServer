import React from 'react';
import Video from './video';
import VideoList from './videolist'

class Stream extends React.Component {
  constructor(props) {
    super(props);

    this.handleVideoPicked = this.handleVideoPicked.bind(this);

    this.state = { 
      currentUrl: "IMG_2202.MOV",
    };
  }

  componentDidMount() {
  }

  handleVideoPicked(new_video_url) {
    // Update button state
    this.setState({ currentUrl: new_video_url});
  }

  render() {
    return (
      <div className="stream">
        <Video url={"/uploads/" + this.state.currentUrl} />
        <p>{this.state.currentUrl}</p>
        <button>Next</button>
        <button>Prev</button>
        <VideoList onClick={this.handleVideoPicked}/>
      </div>
    );
  }
}

Stream.propTypes = {
};

export default Stream;
