export const state = () => ({
  assets: [],
  liabilities: []
})

export const mutations = {
  async add(state, data) {
    const acc = {
      account_type: data.account.type,
      name: data.name,
      account_name: data.account.name,
      balance: data.balance
    }
    await this.$axios.post('/accounts', acc);

    if (data.account.type == 'liability') {
      state.liabilities.push(data)
    } else if (data.account.type == 'asset') {
      state.assets.push(data)
    }
  },
  async getAccounts(state) {
    let res = await this.$axios.get('/accounts')
    res.data.accounts.forEach((account) => {
      state.assets.push({
        name: account.name,
        account: {name: account.account_name, type: account.account_type},
        balance: account.balance
      });
    })
  }
  // remove(state, { todo }) {
  //   state.accounts.splice(state.accounts.indexOf(todo), 1)
  // }
}

export const actions = {}
