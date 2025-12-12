import { createSlice, PayloadAction } from '@reduxjs/toolkit';

const initialState = {
    email: null,
};

const setLocalEmailState = (state, action: PayloadAction<any>) => {
  state.email = action.payload;
};

const slice = createSlice({
  name: 'login',
  initialState,
  reducers: {
    setLocalEmail: setLocalEmailState,
  },
});

export const { setLocalEmail } = slice.actions;

export default slice.reducer;