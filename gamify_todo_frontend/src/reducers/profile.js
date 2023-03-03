import {
    LOAD_USER_PROFILE_FAIL,
    LOAD_USER_PROFILE_SUCCESS
} from '../actions/types';

const initialState = {
    username: '',
    first_name: '',
    email: ''
}

export default function(state = initialState, action) {
    const { type, payload } = action;
    switch(type){
        case LOAD_USER_PROFILE_SUCCESS:
            return {
                ...state,
                username: payload.username,
                first_name: payload.profile.first_name,
                email: payload.profile.email
            }
        case LOAD_USER_PROFILE_FAIL:
            return {
                ...state,
                username: '',
                first_name: '',
                email: ''
            }
        default:
            return state
    }
};