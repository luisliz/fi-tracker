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
  async getAccounts(state) {
    let res = await this.$axios.get('/accounts')
    console.log(res.data.accounts)
    res.data.accounts.forEach((account) => {
      state.assets.push(account);
    })
  }
  // remove(state, { todo }) {
  //   state.accounts.splice(state.accounts.indexOf(todo), 1)
  // }
}

export const actions = {

}
