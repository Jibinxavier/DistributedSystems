import React from 'react';

const FileList = props => {
  if (!props.files) {
    return (
      <div className="file-preview">Loading....</div>
    );
  }
  if (props.files.length === 0){
    return (
      <div className="file-preview">
        no files here...
      </div>
    );

  }
  return (
    <div>
      {
        props.files.map( file =>{
          return (
            <h2>{file.name}</h2>
          );
        })
      }
    </div>
  )
}
export default FileList;