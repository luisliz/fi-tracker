import merge from "lodash.merge";
import assign from 'lodash.assign';

export const state = () => ({
  categories: [],
  category: {},
});

export const mutations = {
  set(state, category) {
    state.categories = category
  },
  add(state, value) {
    merge(state.categories, value)
  },
  remove(state, {category}) {
    state.categories.filter(c => category.id !== c.id)
  },
  mergeCars(state, form) {
    assign(state.category, form)
  },
  setCars(state, form) {
    state.category = form
  }
};

export const actions = {
  async get({commit}) {
    await this.$axios.get(`/budget/category`)
      .then((res) => {
        if (res.status === 200) {
          commit('set', res.data)
        }
      })
  },
  async show({commit}, params) {
    await this.$axios.get(`/categorys/${params.category_id}`)
      .then((res) => {
        if (res.status === 200) {
          commit('mergeCars', res.data)
        }
      })
  },
  async set({commit}, categorys) {
    await commit('set', categorys)
  },
  async form({commit}, form) {
    await commit('mergeCars', form)
  },
  async add({commit}, category) {
    await commit('add', category)
  },
  create({commit}, params) {
    return this.$axios.post(`/budget/category`, params)
  },
  // update({commit}, params) {
  //   return this.$axios.put(`/categorys/${params.id}`, {category: params})
  // },
  // delete({commit}, params) {
  //   return this.$axios.delete(`/categorys/${params.id}`)
  // }
};
