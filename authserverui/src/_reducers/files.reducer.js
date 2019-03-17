import { filesConstants } from '../_constants';

export function files(state = {}, action) {
  console.log(filesConstants)
  switch (action.type) {
    case filesConstants.GETALL_REQUEST:
      return {
        loading: true
      };
    case filesConstants.GETALL_SUCCESS:
      return {
        items: action.files
      };
    case filesConstants.GETALL_FAILURE:
      return { 
        error: action.error
      };
    case filesConstants.DELETE_REQUEST:
      // add 'deleting:true' property to file being deleted
      return {
        ...state,
        items: state.items.map(file =>
          file.id === action.id
            ? { ...file, deleting: true }
            : file
        )
      };
    case filesConstants.DELETE_SUCCESS:
      // remove deleted file from state
      return {
        items: state.items.filter(file => file.id !== action.id)
      };
    case filesConstants.DELETE_FAILURE:
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