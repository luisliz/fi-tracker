import merge from "lodash.merge";
import assign from 'lodash.assign';

export const state = () => ({
  entries: [],
  entry: {},
});

export const mutations = {
  set(state, entry) {
    state.entries = entry
  },
  add(state, value) {
    merge(state.entries, value)
  },
  remove(state, {entry}) {
    state.entries.filter(c => entry.id !== c.id)
  },
  // mergeCars(state, form) {
  //   assign(state.entry, form)
  // },
  setCars(state, form) {
    state.entry = form
  }
};

export const actions = {
  async get({commit}) {
    await this.$axios.get(`/cars`)
      .then((res) => {
        if (res.status === 200) {
          commit('set', res.data)
        }
      })
  },
  // async show({commit}, params) {
  //   await this.$axios.get(`/cars/${params.car_id}`)
  //     .then((res) => {
  //       if (res.status === 200) {
  //         commit('mergeCars', res.data)
  //       }
  //     })
  // },
  async set({commit}, entries) {
    await commit('set', entries)
  },
  // async form({commit}, form) {
  //   await commit('mergeCars', form)
  // },
  async add({commit}, entry) {
    await commit('add', entry)
  },
  create({commit}, params) {
    return this.$axios.post(`/budget`, {budget: params})
  },
  // update({commit}, params) {
  //   return this.$axios.put(`/cars/${params.id}`, {car: params})
  // },
  // delete({commit}, params) {
  //   return this.$axios.delete(`/cars/${params.id}`)
  // }
};
