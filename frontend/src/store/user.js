export const state = () => ({
    id:0,
    username:"",
    email:"",
    password:"",
    job_title:""
})

export const mutations = {
    storeId: (state, data) => {
        state.id = data
    },
    storeUsername: (state, data) => {
        state.username = data
    },
    storeEmail: (state, data) => {
        state.email = data
    },
    storePassword: (state, data) => {
        state.password = data
    },
    storeJob_title: (state, data) => {
        state.job_title = data
    }
}