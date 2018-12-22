import React from 'react';

class VideoList extends React.Component {
  constructor(props) {
    super(props);

    this.handleVideoClick = props.onClick

    this.state = { 
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

  render() {
    return (
      <div className="videoList">
        <ul>
          {
          this.state.videos.map((videoName, index) =>
            <li key={index}><button onClick={() => this.handleVideoClick(videoName)}>{videoName}</button></li>)
            }
        </ul>
      </div>
    );
  }
}

VideoList.propTypes = {
};

export default VideoList;
