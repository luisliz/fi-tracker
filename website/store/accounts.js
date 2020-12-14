export const state = () => ({
  assets: [],
  liabilities: []
})

export const mutations = {
  add(state, data) {
    if (data.account.type == 'liability') {
      state.liabilities.push(data)
    } else if (data.account.type == 'asset') {
      state.assets.push(data)
    }
  },
  // remove(state, { todo }) {
  //   state.accounts.splice(state.accounts.indexOf(todo), 1)
  // }
}
