import React from 'react';
import FilePreview from './FilePreview';
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
            <FilePreview file={file} />
          );
        })
      }
    </div>
  )
}
export default FileList;