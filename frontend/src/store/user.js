export const state = () => ({
    id:0,
    username:"",
    lastname:"",
    email:"",
    password:"",
    position:""
})

export const mutations = {
    storeId: (state, data) => {
        state.id = data
    },
    storeUsername: (state, data) => {
        state.username = data
    },
    storeLastname: (state, data) => {
        state.lastname = data
    },
    storeEmail: (state, data) => {
        state.email = data
    },
    storePassword: (state, data) => {
        state.password = data
    },
    storePosition: (state, data) => {
        state.position = data
    }
}