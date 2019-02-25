import React from 'react';

const FilePreview = props => {
    const file = props.file;

    return (
        <div className="file-preview">
            <div className="file-meta">
                <a>
                <img src={file.author.image} />

                </a>
                <div className="info">
          <a className="author">
            {file.author.username}
          </a>
          <span className="date">
            {new Date(file.createdAt).toDateString()}
          </span>
        </div>

        <div className="pull-xs-right">
          <button
            className="btn btn-sm btn-outline-primary">
            <i className="ion-heart"></i> {file.favoritesCount}
          </button>
        </div>
      </div>

      <a to={`file/${file.slug}`} className="preview-link">
        <h1>{file.title}</h1>
        <p>{file.description}</p>
        <span>Read more...</span>
        <ul className="tag-list">
          {
            file.tagList.map(tag => {
              return (
                <li className="tag-default tag-pill tag-outline" key={tag}>
                  {tag}
                </li>
              )
            })
          }
        </ul>
      </a>
    </div>
  );
}

export default FilePreview;