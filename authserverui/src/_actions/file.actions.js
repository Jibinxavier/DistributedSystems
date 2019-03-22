import { fileConstants } from '../_constants';
import { fileService } from '../_services';
import { alertActions } from './';
import { history } from '../_helpers';

export const fileActions = {
    upload,
    download, 
    listAll,
    delete: _delete
};

function upload(localFilepath){
    return dispatch =>{
        dispatch(request({ localFilepath}));
        fileService.upload(localFilepath)
            .then (
                file => {

                   
                    dispatch(success(file))
                    history.push('/'); // to return back to home page
                },
                error => {
                    dispatch(failure(error.toString()));
                    dispatch(alertActions.error(error.toString()));
                }
            )

    }
    function request(file) { return { type: fileConstants.UPLOAD_FILE_REQUEST, file}}
    function success(file) { return { type: fileConstants.UPLOAD_FILE_SUCCESS, file}}
    function failure(file) { return { type: fileConstants.UPLOAD_FILE_FAILURE, file}}
}

function download(localFilepath){
    return dispatch =>{
        dispatch(request({ localFilepath}));
        fileService.upload(localFilepath)
            .then (
                file => {
                    dispatch(success(file))
                    history.push('/'); // to return back to home page
                },
                error => {
                    dispatch(failure(error.toString()));
                    dispatch(alertActions.error(error.toString()));
                }
            )

    }
    function request(file) { return { type: fileConstants.UPLOAD_FILE_REQUEST, file}}
    function success(file) { return { type: fileConstants.UPLOAD_FILE_SUCCESS, file}}
    function failure(file) { return { type: fileConstants.UPLOAD_FILE_FAILURE, file}}
}

function listAll(localFilepath){
    return dispatch =>{
        dispatch(request({ localFilepath}));
        fileService.upload(localFilepath)
            .then (
                file => {
                    dispatch(success(file))
                    history.push('/'); // to return back to home page
                },
                error => {
                    dispatch(failure(error.toString()));
                    dispatch(alertActions.error(error.toString()));
                }
            )

    }
    function request(file) { return { type: fileConstants.UPLOAD_FILE_REQUEST, file}}
    function success(file) { return { type: fileConstants.UPLOAD_FILE_SUCCESS, file}}
    function failure(file) { return { type: fileConstants.UPLOAD_FILE_FAILURE, file}}
}

function _delete(){
    
}