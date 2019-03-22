import { fileConstants } from '../_constants';

export function files(state = {}, action) {
  console.log(fileConstants)
  switch (action.type) {
    case fileConstants.UPLOAD_FILE_REQUEST:
      return {
        loading: true
      };
    case fileConstants.UPLOAD_FILE_SUCCESS:
      return {
        items: action.files
      };
    case fileConstants.UPLOAD_FILE_FAILURE:
      return { 
        error: action.error
      };
    case fileConstants.DELETE_REQUEST:
      // add 'deleting:true' property to file being deleted
      return {
        ...state,
        items: state.items.map(file =>
          file.id === action.id
            ? { ...file, deleting: true }
            : file
        )
      };
    case fileConstants.DELETE_SUCCESS:
      // remove deleted file from state
      return {
        items: state.items.filter(file => file.id !== action.id)
      };
    case fileConstants.DELETE_FAILURE:
      // remove 'deleting:true' property and add 'deleteError:[error]' property to file 
      return {
        ...state,
        items: state.items.map(file => {
          if (file.id === action.id) {
            // make copy of file without 'deleting:true' property
            const { deleting, ...fileCopy } = file;
            // return copy of file with 'deleteError:[error]' property
            return { ...fileCopy, deleteError: action.error };
          }

          return file;
        })
      };
    default:
      return state
  }
}