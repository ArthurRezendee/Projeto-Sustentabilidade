const baseUrl = 'http://localhost'

const instance_api = axios.create({
    baseURL: `${baseUrl}:5000/sustainability`,
    headers: {
        'Content-Type': 'application/json',
    },
});

function getAxiosInstance() {
    return instance_api;
}