import React from 'react';
import Video from './video';
import VideoList from './videolist'

class Stream extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="stream">
        <Video />
        <button>Next</button>
        <button>Prev</button>
        <VideoList />
      </div>
    );
  }
}

Stream.propTypes = {
};

export default Stream;
