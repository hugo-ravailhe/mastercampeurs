import React from 'react';
import {Image, View} from 'react-native';

const Logo = () => {
  return (
    <View>
      <Image
        resizeMode="contain"
        style={{height: 100, width: 100}}
        source={require('C:\\Prg\\mastercampeurs\\react\\mastercampeurs\\src\\component\\logo.png')}
      />
    </View>
  );
};

export default Logo;
