import { uploadPhoto, createUser } from './utils.js';

export default async function asyncUploadUser() {
    return Promise.all([uploadPhoto(), createUser()])
    
}