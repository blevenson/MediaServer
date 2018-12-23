import React from 'react';

class VideoList extends React.Component {
  constructor(props) {
    super(props);

    this.handleVideoClick = props.onClick
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="videoList">
        <ul>
          {
          this.props.videos.map((video, index) =>
            <li key={index}><button className={video.watched ? "watched" : "unwatched"} onClick={() => this.handleVideoClick(video)}>{video.title}</button></li>)
            }
        </ul>
      </div>
    );
  }
}

VideoList.propTypes = {
};

export default VideoList;
