import React from 'react';

class VideoList extends React.Component {
  constructor(props) {
    super(props);

    this.state = { 
      videos: ["Season 1 Episode 1", "Season 1 Episode 2", "Season 1 Episode 3"],
    };
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="videoList">
        <ul>
          {
          this.state.videos.map((videoName, index) =>
            <li key={index}>{videoName}</li>)
            }
        </ul>
      </div>
    );
  }
}

VideoList.propTypes = {
};

export default VideoList;
