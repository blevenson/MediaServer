import React from 'react';
import Video from './video';
import VideoList from './videolist'

class Stream extends React.Component {
  constructor(props) {
    super(props);

    this.handleVideoPicked = this.handleVideoPicked.bind(this);
    this.handleDeleteVideo = this.handleDeleteVideo.bind(this);

    this.state = { 
      currentVideo: {
        "description": "Ranger next to kitchen table looking up.", 
        "file": "56694509373__7DAD3424-4D27-4B9F-B489-4F419F52FF2B.MOV", 
        "title": "Ranger Looking", 
        "videoid": 1, 
        "watched": 0
      },
      videos: [],
    };

    fetch("/api/v1/videos/")
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      return response.json();
    })
    .then((data) => {
      this.setState({
        videos: data.videos
      });
    })
    .catch(error => console.log(error));
  }

  componentDidMount() {
  }

  handleVideoPicked(new_video) {
    this.setState({ currentVideo: new_video});

    fetch('/api/v1/watched/', {
      method: new_video["watched"] ? 'DELETE' : 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify(new_video),
    })

    new_video['watched'] = new_video['watched'] ? 0 : 1;
  }

  handleDeleteVideo() {

    // Check to confirm
    var r = confirm("Are you sure you want to delete?");
    if (r != true) {
      return;
    }

    // Update db
    fetch('/api/v1/video/' + this.state.currentVideo.videoid, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify({}),
    })

    var array = [...this.state.videos]; // make a separate copy of the array
    var index = array.indexOf(this.state.currentVideo)
    if (index !== -1) {
      array.splice(index, 1);
      this.setState({videos: array});
    }

    this.setState({ currentVideo: array[0]});
  }

  render() {
    return (
      <div className="stream">
        <Video vid={this.state.currentVideo} />
        <p>{this.state.currentVideo.title}</p>
        <button>Prev</button>
        <button className="deleteButton" onClick={this.handleDeleteVideo}>Delete</button>
        <button>Next</button>
        <VideoList videos={this.state.videos} onClick={this.handleVideoPicked} />
      </div>
    );
  }
}

Stream.propTypes = {
};

export default Stream;
