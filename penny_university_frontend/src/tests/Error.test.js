import reducer from '../reducers'
import fetchMock from 'fetch-mock'
import {makeMockStore, initialState} from './config'
import {loadChatsList} from '../actions'

describe('error reducer', () => {
  fetchMock.get('*', () => {
    throw new Error('It failed!')
  })

  it('should put error message in state', () => {
    const store = makeMockStore()

    return store.dispatch(loadChatsList('1')).then(() => {
      const state = reducer(initialState, store.getActions()[1])
      expect(state.error).toEqual('It failed!')
    })
  })
})
